#!/usr/bin/node
// star wars api

const axios = require('axios');

const movieTitles = {
    1: "A New Hope",
    2: "The Empire Strikes Back",
    3: "Return of the Jedi",
    4: "The Phantom Menace",
    5: "Attack of the Clones",
    6: "Revenge of the Sith",
    7: "The Force Awakens",
    8: "The Last Jedi",
    9: "The Rise of Skywalker"
};

const movieId = process.argv[2];

if (!movieId || !movieTitles[movieId]) {
    console.error("Please provide a valid Movie ID as the first argument.");
    process.exit(1);
}

const getFilmData = async (movieId) => {
    try {
        const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
        return response.data;
    } catch (error) {
        console.error("Error fetching film data:", error);
        process.exit(1);
    }
};

const getCharacterNames = async (characterUrls) => {
    try {
        const characterPromises = characterUrls.map(url => axios.get(url));
        const characterResponses = await Promise.all(characterPromises);
        return characterResponses.map(response => response.data.name);
    } catch (error) {
        console.error("Error fetching character data:", error);
        process.exit(1);
    }
};

const printCharacters = async (movieId) => {
    const filmData = await getFilmData(movieId);
    const characterNames = await getCharacterNames(filmData.characters);
    characterNames.forEach(name => console.log(name));
};

printCharacters(movieId);