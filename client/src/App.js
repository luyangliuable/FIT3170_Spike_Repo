import logo from './logo.svg';
import react, {useState, useEffect} from 'react';
import './App.css';


const card_style = {
    'border': '2px solid black',
    'cursor': 'pointer',
    'borderRadius': '2px',
    'color': 'white',
    'background': '#1e90ff',
    'display': 'flex-box',
    'padding': '20px',
    'width': '500px',
    'padding': '50px 0px 50px 0px',
    'textAlign': 'center',
};

const container_style = {
    'display': 'flex',
    'alignContent': 'center',
    'alignItems': 'center',
    'justifyContent': 'space-around',

    // 'background': 'yellow',
};

const increaseIndex = (change, displayIndex, questions) => {
    console.log(questions);
    if (displayIndex + 1 >= questions.length){
        change(0);
        console.log("reached final interview question");
    } else {
        change(displayIndex + 1);
    }
}


const App = () => {
    const [questions, setQuestions] = useState([{}]);
    const [displayIndex, changeIndex] = useState(0);


    useEffect(() => {
        fetch("/members").then(
            res => res.json()
        ).then( data => {
            setQuestions(data);
            console.log(data);
        });
    }, []);



    return (
        <>
            <h1>Flashcards:</h1>
            Displaying card: { displayIndex ? displayIndex : "first card" }
            <div className='container' style={container_style}>
            { questions?.filter((member, index) => index === displayIndex).map(( member,index ) => (
                <div className='flashcards' style={ card_style }>
                    { member['question'] }
                </div>
            )) }
            </div>

            <button onClick={() => increaseIndex(changeIndex, displayIndex, questions)}>Next</button>
        </>
    );
}


export default App;
