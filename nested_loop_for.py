peoples ={
    "Ahmed": {
         "Html": "70%",
         "CSS": "60%",
         "JS": "90%"
    }, 
    "Dina": {
        "Html": "30%",
         "CSS": "40%",
         "JS": "100%"

    },
    "Mohamed": {
         "Html": "10%",
         "CSS": "20%",
         "JS": "50%"
    }
}

for name in peoples:
    print (f"skills for {name}: ")

    for skill in peoples[name]:
        print (f"-{peoples[name][skill]}")