import tv

def main():
    print("Create TV set")
    my_tv = tv.TV()

    print("Show TV status")
    my_tv.show_status()

    print("Turn TV on")
    my_tv.turn_on()
    my_tv.show_status()

    print("Turn TV off")
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
    main()
