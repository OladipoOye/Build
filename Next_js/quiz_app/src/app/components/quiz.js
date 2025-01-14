"use client"

import { useState, useEffect } from "react";


export default function Quiz(props) {
    const [input, setInput] = useState(''); //for the user input values
    const [current, setCurrent] = useState(0); // for the current level
    const [streak, setStreak] = useState(0); // for the streak
    const [error, setError] = useState(false);
    const [maxStreak, setMaxStreak] = useState(0);
    
    const list = props.q;
    const name = props.name;
    const que = props.opt1;
    const ans = props.opt2;
    console.log('que, ans is', que, ans);
    //console.log('list is', list)
    
    //for the random questions
    const randomize = () => {
        const rIndex = Math.floor(Math.random() * list.length);
        setCurrent(rIndex);
    }
    
    //for the imputs
    const handleChange = evt => {
        setInput(evt.target.value);
    }
    
    
    // for the question handling
    const handleSubmit = evt => {
        evt.preventDefault();

        if (input.toLowerCase() === list[current][ans]) {
            setStreak((prev) => prev + 1);
            setMaxStreak((prev) => prev + 1);
            
            setError(false);

            localStorage.setItem('streak', streak + 1);
            localStorage.setItem('maxStreak', Math.max(streak, maxStreak));
        } else {
            setError(`wrong, the correct answer for ${list[current][que]} is ${list[current][ans]} `);
            setStreak(0);

            localStorage.setItem('streak', 0);

        }

        setInput('');
        randomize();
    }
    
    useEffect( () => {
        randomize();
        setStreak(parseInt(localStorage.getItem('streak')) || 0);
        setMaxStreak(parseInt(localStorage.getItem('maxStreak')) || 0);
        console.log('the question is', list[current][que]);
    }, [])
    
    
    return (
        <div>
            <header>
                <h1> {name} Quiz</h1>
                <div>
                    <p> {streak} / {maxStreak} </p>
                </div>
            </header>
            
            <div>
                {list[current][que]}
            </div>
            
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={input}
                    onChange={handleChange} />
            </form>
            
            {error && <p>{error}</p>}
        </div>
    );
}