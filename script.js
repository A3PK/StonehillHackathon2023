const quizData = [{
    question: "If you get diarrhea, which foods are best to eat",
    a: "Foods high in potassium",
    b: "Foods high in sugar",
    c: "Foods that are very spicy",
    d: "Fatty Foods",
    correct: "a",
}, {
    question: "What is the name of the virus that causes flu",
    a: "Epstein–Barr virus",
    b: "Influenza",
    c: "Pink Eye",
    d: "Coxsackievirus",
    correct: "b",
}, {
    question: "What is the scientific name of pink eye?",
    a: "Pieselilo",
    b: "Coutrtoisleois",
    c: "Conjunctivitis",
    d: "Konjunctivitis",
    correct: "c",
}, {
    question: "When was the first virus discovered?",
    a: "1900",
    b: "1891",
    c: "1893",
    d: "1892",
    correct: "d",
}, {
    question: "Scientific name for sinusitis?",
    a: " Acute rhinosinusitis",
    b: "Rhinosinusitis",
    c: "Aroot rhinosinusitis",
    d: "Acoot rhinosinusitis",
    correct: "a",
}, {
    question: "What is obesity?",
    a: " When you are too skinny",
    b: "When you are overweight",
    c: "When you have a body index over 25",
    d: "When you are malnourished",
    correct: "c",
}
];

const quiz = document.getElementById('quiz');
const answerEls = document.querySelectorAll('.answer');
const questionEl = document.getElementById('question');
const a_text = document.getElementById('a_text');
const b_text = document.getElementById('b_text');
const c_text = document.getElementById('c_text');
const d_text = document.getElementById('d_text');
const submitBtn = document.getElementById('submit');

let currentQuiz = 0;
let score = 0;

loadQuiz();

function loadQuiz() {
    deselectAnswer();

    const currentQuizData = quizData[currentQuiz];

    questionEl.innerText = currentQuizData.question;
    a_text.innerText = currentQuizData.a;
    b_text.innerText = currentQuizData.b;
    c_text.innerText = currentQuizData.c;
    d_text.innerText = currentQuizData.d;
}

function deselectAnswer() {
    answerEls.forEach(answerEl => answerEl.checked = false);
}

function getSelected() {
    let answer;

    answerEls.forEach(answerEl => {
        if (answerEl.checked) {
            answer = answerEl.id;
        }
    });

    return answer;
}

submitBtn.addEventListener('click', () => {
    const answer = getSelected();

    if (answer) {
        if (answer === quizData[currentQuiz].correct) {
            score++;
        }

        currentQuiz++;

        if (currentQuiz < quizData.length) {
            loadQuiz();
        } else {
            quiz.innerHTML = `
        <h2> You answered correctly at ${score}/${quizData.length} questions correctly</h2>

        <button onclick="location.reload()">
        Reload
        </button>
        `
        }
    }
})
