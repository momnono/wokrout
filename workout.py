"""a app that manages a collection of workouts"""
import json

class Workout:
    def __init__(self, name, muscle_group, reps_sets, weight, difficulty):
        self.name = name
        self.muscle_group = muscle_group
        self.reps_sets = reps_sets
        self.weight = weight
        self.difficulty = difficulty

    def __str__(self):
        return f"{self.name} ({self.muscle_group})"


class WorkoutManager:
    def __init__(self, data_file):
        pass

    def create_workout(self):
        pass

    def search_workouts(self):
        pass

    def edit_workout(self):
        pass

    def delete_workout(self):
        pass

    def save_data(self):
        pass

    def run(self):
        pass
