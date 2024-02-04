const question = document.getElementById("question");
const codeBlock = document.getElementById("code-block");
// const choices = Array.from(document.getElementsByClassName("choice-text"));
const choice = document.getElementsByClassName("choice-text")
const choiceContainer = Array.from(document.getElementsByClassName("choice-container"));
const progressText = document.getElementById("progressText");
const progressFull = document.getElementsByClassName("progressBarFull");
const loader = document.getElementById("loader");
const game = document.getElementById("game");

let currentQuestion = {};
let quesitonCounter = 0;
let availableQuestions =[];
let questions = [];
let questionIndex = -1;
let submittedAnswers = {};

const CORRECT_BONUS = 10;

fetch('./questions.json')
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
};

getNewQuestion = () => {
    if (questionCounter >= num_questions) {
        return window.location.assign("index.html");  //go to the end page
    };
    
    questionCounter ++;
    console.log(questionCounter)
    progressText.innerHTML = `Question ${questionCounter}/${num_questions}`;
    progressBarFull.style.width = `${(questionCounter / num_questions) * 100}%`;

    questionIndex++;
    currentQuestion = availableQuestions[questionIndex];
    question.innerHTML = currentQuestion.question;

    // choices.forEach((choice, index) => {
    //     choice.innerText = "Next"
    // });
    choice.innerText = "Next"

    clickAnswer();
};

function clickAnswer() {
    // choices.forEach((choice, index) => {
    //     choice.addEventListener('click', e => {
    //         // setTimeout(() => {
    //         //     getNewQuestion();
    //         // }, 1000);
    //         setTimeout(getNewQuestion, 1000)
    //     });
    // });

    choice.addEventListener("click", function() {
        setTimeout(getNewQuestion, 1000)
    });
}
      
function shuffle(sourceArray) {
    for (var i = 0; i < sourceArray.length - 1; i++) {
        var j = i + Math.floor(Math.random() * (sourceArray.length - i));

        var temp = sourceArray[j];
        sourceArray[j] = sourceArray[i];
        sourceArray[i] = temp;
    }
    return sourceArray;
}