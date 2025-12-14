import tv

def main():
    print("Create TV set")
    my_tv = tv.TV()

    print("Turn TV on")
    my_tv.turn_on()
    my_tv.show_status()

    print("Set TV channels")
    my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "National Geographic"])

    print("Display the list of available channels")
    my_tv.show_channels()

    print("Change TV channel to 4")
    my_tv.set_channel(4)
    my_tv.show_status()

    print("Increase TV volume")
    my_tv.increase_volume()
    my_tv.show_status()

    print("Increase TV volume again")
    my_tv.increase_volume()
    my_tv.show_status()

    print("Decrease TV volume")
    my_tv.decrease_volume()
    my_tv.show_status()

    print("Decrease TV volume to minimum")
    my_tv.decrease_volume()
    my_tv.show_status()

    print("Turn TV off")
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
    main()
