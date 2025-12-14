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

    print("Change TV channel to 2")
    my_tv.set_channel(2)
    my_tv.show_status()

    print("Change TV channel to 7 (out of range)")
    my_tv.set_channel(7)
    my_tv.show_status()

    print("Change TV channel to 6")
    my_tv.set_channel(6)
    my_tv.show_status()

    print("Turn TV off")
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
    main()
