const express = require('express');
const router = express.Router();
const { spawn } = require('child_process');

// render
router.get('/', (req, res) => {
    res.render('index');
});

// router
router.post('/search', (req, res) => {
    const query = req.body.query;
    const python = spawn('python3', ['./scripts/searchBook/main.py', query]);

    let result = '';

    // excute Python 
    python.stdout.on('data', (data) => {
        result += data.toString();
    });

   
    python.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
    });

    // data 
    python.on('close', (code) => {
        try {
            const json = JSON.parse(result); 
            res.render('results', {  
                query: json.query,
                tfidf_recommendations: json.tfidf_recommendations,
                semantic_recommendations: json.semantic_recommendations,
            });
        } catch (err) {
            console.error("Failed to parse JSON:", result);
            res.status(500).send("Error processing request");
        }
    });
});

module.exports = router;
