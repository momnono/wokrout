"""a app that manages a collection of workouts"""
import json

class Workout:
    def __init__(self, name, muscle_group, reps_sets, weight, difficulty):        # Initializes a new workout object with the given properties.

        self.name = name
        self.muscle_group = muscle_group
        self.reps_sets = reps_sets
        self.weight = weight
        self.difficulty = difficulty

    def __str__(self):        # Returns a string representation of the workout object.

        return f"{self.name} ({self.muscle_group})"


class WorkoutManager:
    def __init__(self, data_file):
        self.data_file = data_file
        self.workouts = []
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                for w in data["workouts"]:
                    self.workouts.append(Workout(**w))
        except FileNotFoundError:
            pass

    def create_workout(self):
        print("Creating a new workout...")
        name = input("Name: ")
        muscle_group = input("Muscle group: ")
        reps_sets = input("Reps/Sets: ")
        weight = input("Weight: ")
        difficulty = input("Difficulty: ")
        workout = Workout(name, muscle_group, reps_sets, weight, difficulty)
        self.workouts.append(workout)
        print("Workout created successfully.")




    def search_workouts(self):
        search_term = input("Enter a search term: ")
        matching_workouts = [w for w in self.workouts if search_term.lower() in w.name.lower() or search_term.lower() in w.muscle_group.lower()]
        if matching_workouts:
            for workout in matching_workouts:
                print(f"{workout.name} ({workout.muscle_group})")
        else:
            print("No matching workouts found.")


    def edit_workout(self):
        search_term = input("Enter the name of the workout to edit: ")
        matching_workouts = [w for w in self.workouts if search_term.lower() in w.name.lower()]
        if not matching_workouts:
            print("No matching workouts found.")
            return
        elif len(matching_workouts) > 1:
            print(f"Found {len(matching_workouts)} matching workouts. Please refine your search.")
            return
        workout = matching_workouts[0]
        workout.name = input(f"Name ({workout.name}): ") or workout.name
        workout.muscle_group = input(f"Muscle group ({workout.muscle_group}): ") or workout.muscle_group
        workout.reps_sets = input(f"Reps/Sets ({workout.reps_sets}): ") or workout.reps_sets
        workout.weight = input(f"Weight ({workout.weight}): ") or workout.weight
        workout.difficulty = input(f"Difficulty ({workout.difficulty}): ") or workout.difficulty
        print("Workout edited successfully.")

    def delete_workout(self):
        search_term = input("Enter the name of the workout to delete: ")
        matching_workouts = [w for w in self.workouts if search_term.lower() in w.name.lower()]
        if not matching_workouts:
            print("No matching workouts found.")
            return
        elif len(matching_workouts) > 1:
            print(f"Found {len(matching_workouts)} matching workouts. Please refine your search.")
            return
        workout = matching_workouts[0]
        self.workouts.remove(workout)
        print("Workout deleted successfully.")


    def save_data(self):
        data = {"workouts": [w.__dict__ for w in self.workouts]}
        with open(self.data_file, "w") as f:
            json.dump(data, f)
        print("Data saved successfully.")
    def run(self):
        while True:
            command = input("Enter a command (create, search, edit, delete, exit): ")
            if command == "create":
                self.create_workout()
            elif command == "search":
                self.search_workouts()
            elif command == "edit":
                self.edit_workout()
            elif command == "delete":
                self.delete_workout()
            elif command == "exit":
                self.save_data()
                print("Exiting program.")
                break
            else:
                print("Invalid command.")
        print("Exited while loop.")
if __name__ == '__main__':
    data_file = 'workouts.json'
    manager = WorkoutManager(data_file)
    manager.run()
