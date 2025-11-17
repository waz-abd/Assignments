# input_processing.py
# Abdul Wasay, ENSF 692 Spring 2025 - Assignment #2
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.).
# You may import any modules from the standard Python library.
# Remember to include your name and comments.


# No global variables are permitted

# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Initizaling traffic light, pedistrian status, and vehicle status to default values of green, no, no
    def __init__(self):
        self.traffic_light = "green"
        self.pedestrian_status = "no"
        self.vehicle_status = "no"

    # This is an update status method that updates the attributes of the class. It inputs status input and change input.
    def update_status(self, status_input, change_input):

        if status_input == "1":
            self.traffic_light = change_input

        if status_input == "2":
            self.pedestrian_status = change_input

        if status_input == "3":
            self.vehicle_status = change_input


# This function prints out the action depending on the sensor status. It inputs sensor as its parameter from sensor object.

def print_message(sensor):

    if ((sensor.traffic_light == "red") or (sensor.pedestrian_status == "yes") or (sensor.vehicle_status == "yes")):
        print("\nSTOP")

    if ((sensor.traffic_light == "green") and (sensor.pedestrian_status == "no") and (sensor.vehicle_status == "no")):
        print("\nProceed")

    if ((sensor.traffic_light == "yellow") and (sensor.pedestrian_status == "no") and (sensor.vehicle_status == "no")):
        print("\nCaution")

    print("\nLight = " + sensor.traffic_light, "," + " Pedestrian = " +
          sensor.pedestrian_status, "," + " Vehicle = " + sensor.vehicle_status + "\n")


# This is the main function in which the code runs.
def main():

    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")

    sensor_object = Sensor()

    while True:

        print("Are changes detected in the vision input?")

        status_input = input(
            "Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to the end the program: ")

        # print("\n")

        if ((status_input != '1') and (status_input != "2") and (status_input != "3") and (status_input != "0")):
            print("You must select either 1, 2, 3, or 0.\n")
            continue

        if (status_input == "0"):
            break

        change_input = input("What change has been identified?: ")

        if ((change_input != "green") and (change_input != "red") and (change_input != "yellow") and (change_input != "yes") and (change_input != "no")):
            print("Invalid vision change.")
            print_message(sensor_object)
            continue

        if (status_input == "1"):
            if (change_input != "green") and (change_input != "yellow") and (change_input != "red"):
                print("Invalid vision change.")
                print_message(sensor_object)
                continue

        if ((status_input == "2") or (status_input == "3")):
            if ((change_input != "yes") and (change_input != "no")):
                print("Invalid vision change.")
                print_message(sensor_object)
                continue

        sensor_object.update_status(status_input, change_input)

        print_message(sensor_object)


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()
