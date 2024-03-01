const question = document.getElementById("question");
const codeBlock = document.getElementById("code-block");
const choices = Array.from(document.getElementsByClassName("choice-text"));
const progressText = document.getElementById("progressText");
const progressFull = document.getElementsByClassName("progressBarFull");
const loader = document.getElementById("loader");
const game = document.getElementById("game");

let currentQuestion = {};
let quesitonCounter = 0;
let availableQuestions =[];
let questions = [];
let questionIndex = -1;

var path = window.location.pathname
var page = path.split("/").pop()
if (page == "behavioral.html") {
    var question_file = './behavioral.json'
}
else if (page == "algorithm.html") {
    var question_file = './algorithm.json'
}
else if (page == "system-design.html") {
    var question_file = './system-design.json'
}
else if (page == "machine-learning.html") {
    var question_file = './machine-learning.json'
}
else if (page == "machine-learning-system-design.html") {
    var question_file = './machine-learning-system-design.json'
}
else if (page == "platform-engineering.html") {
    var question_file = './platform-engineering.json'
}

fetch(question_file)
.then(res => {
    return res.json(); 
})
.then(loadedQuestions => {
    questions = loadedQuestions;
    num_questions = Object.keys(questions).length;
    startGame();
}).catch( err => {
    console.error(err);
})

startGame = () => {
    questionCounter = 0;
    availableQuestions = shuffle(questions);

    getNewQuestion();
    game.classList.remove("hidden");
    loader.classList.add("hidden");

    choices.forEach((choice, index) => {
        choice.addEventListener('click', e => {
            setTimeout(getNewQuestion, 500)
        });
    });
};

getNewQuestion = () => {
    if (questionCounter >= num_questions) {
        return window.location.assign("index.html");  //go to the end page
    };
    
    questionCounter ++;
    progressText.innerHTML = `Question ${questionCounter}/${num_questions}`;
    progressBarFull.style.width = `${(questionCounter / num_questions) * 100}%`;

    questionIndex++;
    currentQuestion = availableQuestions[questionIndex];
    question.innerHTML = currentQuestion.question;

    choices.forEach((choice, index) => {
        choice.innerText = "Next"
    });
};
      
function shuffle(sourceArray) {
    for (var i = 0; i < sourceArray.length - 1; i++) {
        var j = i + Math.floor(Math.random() * (sourceArray.length - i));

        var temp = sourceArray[j];
        sourceArray[j] = sourceArray[i];
        sourceArray[i] = temp;
    }
    return sourceArray;
}