Calculate: sustainability score based on user's answers
let score = 0;
if (kwhPerMonth <= 300) {
    score += 10;
} else if (kwhPerMonth <= 600) {
    score += 5;
}
if (numPeople <= 2) {
    score += 10;
} else if (numPeople <= 4) {
    score += 5;
}
if (acUsage === 'none') {
    score += 10;
} else if (acUsage === 'occasionally') {
    score += 5;
}
if (lightingType === 'led') {
    score += 10;
} else if (lightingType === 'fluorescent') {
    score += 5;
}
if (waterHeaterType === 'solar') {
    score += 10;
}
