data = {

    "111" : {

        "name": "anil",
        "mark" : [22, 33, 44]

    },

    "222": {

        "name": "kabeer",
        "mark": [44, 21, 44]

    }
}


for k, v in data.items ():
    t = 0
    print (v ['mark'] )
    for m in  v ['mark'] :
        t = t + m

    print (k, v['name'], t )
