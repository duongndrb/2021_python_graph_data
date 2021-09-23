from matplotlib import pyplot
#from matplotlib.lines import _LineStyle


def draw_multiline():
    years = [2013,2014,2015,2016,2017,2018,2019,2020]
    companyA = [41596,46000,48510,53310,57200,56000,63316,69741]
    companyB = [37956,42000,45510,47310,51200,55000,60316,64741]
    companyC = [36956,32100,49510,30310,54200,45000,68316,34741]
    # color: mau theo rgb
    # linestyle: '--' net dut / '-' net thang(solid)
    #pyplot.plot(years,companyA, color='red', linestyle='--', marker='.', markersize=20)
    #pyplot.show()

    ## Sketch-style drawing mode
    #pyplot.xkcd()

    # style
    #pyplot.style.use('dark_background')

    pyplot.plot(years,companyA, color='red', linestyle='--', marker='.', markersize=20)
    pyplot.plot(years,companyB, color='#000BFF', marker='.', markersize=10)
    pyplot.bar(years,companyC, color='#B40062')

    # gan tieu de cho truc
    pyplot.xlabel("Year")
    pyplot.ylabel("Profit(USD)")

    # chu thich do thi
    pyplot.legend(["Company A","Company B","Company C"])
    # hien thi luoi
    pyplot.grid(True)

    # take photograph
    pyplot.savefig("multiline.png")

    pyplot.show()