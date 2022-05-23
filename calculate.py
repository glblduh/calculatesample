from math import sqrt

if __name__ == "__main__":

    # Get all data
    datas = []
    print("Enter all data, enter DONE if finished")
    while True:
        inp = input("Enter data: ")
        if inp == "DONE":
            break
        datas.append(int(inp))

    # Calculate sample mean
    sum = 0
    for data in datas:
        sum += data
    smean = sum / len(datas)
    print("Sample mean:", smean, "Rounded:", round(smean, 2))

    # Calculate variance
    sum = 0
    for data in datas:
        sum += (data-smean)**2
    svariance = sum / (len(datas)-1)
    print("Sample variance:", svariance, "Rounded:", round(svariance, 2))

    # Calculate standard deviation
    sd = sqrt(svariance)
    print("Sample standard deviation:", sd, "Rounded:", round(sd, 2))