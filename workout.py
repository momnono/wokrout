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
        pass

    def delete_workout(self):
        pass

    def save_data(self):
        pass

    def run(self):
        pass
