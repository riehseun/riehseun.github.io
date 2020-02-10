var my_image_src2016 = "../img/family/me2016.png"
var my_image_src2017 = "../img/family/me2017.png"
var my_image_src2018 = "../img/family/me2018.png"
var my_image_src2019 = "../img/family/me2019.png"
var mom_image_src2016 = "../img/family/mom2016.png"
var mom_image_src2017 = "../img/family/mom2017.png"
var mom_image_src2018 = "../img/family/mom2018.png"
var mom_image_src2019 = "../img/family/mom2019.png"
var aunt_image_src2016 = "../img/family/aunt2016.png"
var aunt_image_src2017 = "../img/family/aunt2017.png"
var aunt_image_src2018 = "../img/family/aunt2018.png"
var aunt_image_src2019 = "../img/family/aunt2019.png"
var sokcho_image_src2016 = "../img/family/sokcho2016.png"
var sokcho_image_src2017 = "../img/family/sokcho2017.png"
var sokcho_image_src2018 = "../img/family/sokcho2018.png"
var sokcho_image_src2019 = "../img/family/sokcho2019.png"

var kakaotalk_dir = "media/"

function get(message, when, my_image_src, type, who) {
    var container = $("<div>")
    if (who == "you") {
        container.addClass("container")
    } else {
        container.addClass("container darker")
    }

    var img = $("<img>")
    img.attr("src", my_image_src)
    if (who != "you") {
        img.addClass("right")
    }

    if (type == "text") {
        var p = $("<p>")
        p.text(message)
    } else if (type == "image") {
        var image = $("<img>")
        image.attr("src", kakaotalk_dir + message)
        image.attr("id", "real-image")
    } else if (type == "video") {

    } else {

    }

    var span = $("<span>")
    span.addClass("time-right")
    span.text(when)

    container.append(img)
    if (type == "text") {
        container.append(p)
    } else if (type == "image") {
        container.append(image)
    } else if (type == "video") {
        container.append(add_video(kakaotalk_dir + message, container))
    } else {

    }
    container.append(span)

    $("body").append(container)
}

function add_video(path, container) {
    var x = document.createElement("VIDEO")

    if (x.canPlayType("video/mp4")) {
        x.setAttribute("src", path)
    } else if (x.canPlayType("video/m4a")) {
        console.log("This is audio")
    } else {
        console.log("What the fuck")
    }
    x.setAttribute("width", "500")
    x.setAttribute("controls", "controls")
    return x
}

window.onload = function() {
    var months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    var message = null
    var who = "you"
    var when = null
    var year = null
    var my_image_src = null
    var mom_image_src = null
    var aunt_image_src = null
    var sokcho_image_src = null

    chat.split(/\r?\n/).forEach(function(line) {
        // Run if it is not an empty line
        if (line) {
            // Check if the first string is month
            var first_letter = line.split(" ")[0]

            if (months.includes(first_letter)) {
                var split_by_colon = line.split(" : ")
                message = split_by_colon[1]

                if (message != null) {
                    var first_part = split_by_colon[0]
                    var first_part_array = first_part.split(",")
                    who = first_part_array[3]
                    year = first_part_array[1].trim()
                    if (year == "2016") {
                        my_image_src = my_image_src2016
                        mom_image_src = mom_image_src2016
                        aunt_image_src = aunt_image_src2016
                        sokcho_image_src = sokcho_image_src2017
                    } else if (year == "2017") {
                        my_image_src = my_image_src2017
                        mom_image_src = mom_image_src2017
                        aunt_image_src = aunt_image_src2017
                        sokcho_image_src = sokcho_image_src2017
                    } else if (year == "2018") {
                        my_image_src = my_image_src2018
                        mom_image_src = mom_image_src2018
                        aunt_image_src = aunt_image_src2018
                        sokcho_image_src = sokcho_image_src2017
                    } else if (year == "2019") {
                        my_image_src = my_image_src2018
                        mom_image_src = mom_image_src2018
                        aunt_image_src = aunt_image_src2018
                        sokcho_image_src = sokcho_image_src2017
                    } else if (year == "2020") {
                        my_image_src = my_image_src2018
                        mom_image_src = mom_image_src2018
                        aunt_image_src = aunt_image_src2018
                        sokcho_image_src = sokcho_image_src2017
                    }
                    when = first_part_array[0] + ", " + first_part_array[1] + ", " + first_part_array[2]
                    // If my message
                    var last_four = message.substr(message.length - 4)
                    if (who.trim() == "you") {
                        if (last_four == ".jpg") {
                            get(message.trim(), when, my_image_src, "image", who.trim())
                        }
                        else if (last_four == ".mp4" || last_four == ".m4a") {
                            get(message.trim(), when, my_image_src, "video", who.trim())
                        }
                        else {
                            get(message.trim(), when, my_image_src, "text", who.trim())
                        }
                    }
                    // If mom's message
                    else if (who.trim() == "mom") {
                        if (last_four == ".jpg") {
                            get(message.trim(), when, mom_image_src, "image", who.trim())
                        }
                        else if (last_four == ".mp4" || last_four == ".m4a") {
                            get(message.trim(), when, mom_image_src, "video", who.trim())
                        }
                        else {
                            get(message.trim(), when, mom_image_src, "text", who.trim())
                        }
                    }
                    else if (who.trim() == "aunt") {
                        if (last_four == ".jpg") {
                            get(message.trim(), when, aunt_image_src, "image", who.trim())
                        }
                        else if (last_four == ".mp4" || last_four == ".m4a") {
                            get(message.trim(), when, aunt_image_src, "video", who.trim())
                        }
                        else {
                            get(message.trim(), when, aunt_image_src, "text", who.trim())
                        }
                    }
                    else if (who.trim() == "sokcho") {
                        if (last_four == ".jpg") {
                            get(message.trim(), when, sokcho_image_src, "image", who.trim())
                        }
                        else if (last_four == ".mp4" || last_four == ".m4a") {
                            get(message.trim(), when, sokcho_image_src, "video", who.trim())
                        }
                        else {
                            get(message.trim(), when, sokcho_image_src, "text", who.trim())
                        }
                    }
                }
            }
            else {
                var last_four = line.substr(line.length - 4)
                if (who.trim() == "you") {
                    if (last_four == ".jpg") {
                        get(line.trim(), when, my_image_src, "image", who.trim())
                    }
                    else if (last_four == ".mp4" || last_four == ".m4a") {
                        get(line.trim(), when, my_image_src, "video", who.trim())
                    }
                    else {
                        get(line.trim(), when, my_image_src, "text", who.trim())
                    }
                }
                // If mom's message
                else if (who.trim() == "mom") {
                    if (last_four == ".jpg") {
                        get(line.trim(), when, mom_image_src, "image", who.trim())
                    }
                    else if (last_four == ".mp4" || last_four == ".m4a") {
                        get(line.trim(), when, mom_image_src, "video", who.trim())
                    }
                    else {
                        get(line.trim(), when, mom_image_src, "text", who.trim())
                    }
                }
                else if (who.trim() == "aunt") {
                    if (last_four == ".jpg") {
                        get(line.trim(), when, aunt_image_src, "image", who.trim())
                    }
                    else if (last_four == ".mp4" || last_four == ".m4a") {
                        get(line.trim(), when, aunt_image_src, "video", who.trim())
                    }
                    else {
                        get(line.trim(), when, aunt_image_src, "text", who.trim())
                    }
                }
                else if (who.trim() == "sokcho") {
                    if (last_four == ".jpg") {
                        get(line.trim(), when, sokcho_image_src, "image", who.trim())
                    }
                    else if (last_four == ".mp4" || last_four == ".m4a") {
                        get(line.trim(), when, sokcho_image_src, "video", who.trim())
                    }
                    else {
                        get(line.trim(), when, sokcho_image_src, "text", who.trim())
                    }
                }
            }
        }
    })
}