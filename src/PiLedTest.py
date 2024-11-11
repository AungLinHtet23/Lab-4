import time
from hal import hal_led as led
from hal import hal_input_switch as switch

def main():
    # Initialize LED and switch
    led.init()  # Initialize the LED
    switch.init()  # Initialize the switch

    try:
        while True:
            # Check the position of the switch
            if switch.read_slide_switch() == 1:
                # If switch is in the left position, blink LED at 5 Hz (0.1s interval)
                led.set_output(0, 1)  # Turn LED on
                time.sleep(0.1)
                led.set_output(0, 0)  # Turn LED off
                time.sleep(0.1)
            else:
                # If switch is in the right position, blink LED at 10 Hz for 5 seconds
                start_time = time.time()
                while time.time() - start_time < 5:
                    led.set_output(0, 1)  # Turn LED on
                    time.sleep(0.05)
                    led.set_output(0, 0)  # Turn LED off
                    time.sleep(0.05)
                
                # After 5 seconds, turn the LED off
                led.set_output(0, 0)
                
                # Wait until the switch changes position to avoid re-triggering
                while switch.read_slide_switch() == 0:
                    time.sleep(0.1)  # Check the switch status every 0.1 seconds

    except KeyboardInterrupt:
        # Clean up GPIO settings if the script is interrupted
        led.set_output(0, 0)  # Ensure LED is off
        print("Program terminated")

if __name__ == "__main__":
    main()
