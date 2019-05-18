<script type=text/babel>

let questions = [
                    {q:"what is the result of 5X5", answer:"25", choices:["15","20","25","30"]},
                    {q:"what is the result of 15X5", answer:"75", choices:["55","65","70","75"]},
                    {q:"what is the result of 25X25", answer:"625", choices:["225","425","525","625"]},
                    {q:"what is the result of 17X17", answer:"289", choices:["229","239","279","289"]},
                    {q:"what is the result of 14x30", answer:"420", choices:["120","320","420","520"]},
                    {q:"what is the result of 13X13", answer:"169", choices:["99","139","169","199"]},
                    {q:"what is the result of 11X11", answer:"121", choices:["101","111","121","131"]},
                    {q:"what is the result of 12X12", answer:"144", choices:["104","124","144","164"]},
                    {q:"what is the result of 10X15", answer:"150", choices:["150","155","125","100"]},
                    {q:"what is the result of 8X9", answer:"72", choices:["56","62","63","72"]},

                ]

let length = questions.length

class App extends React.Component{
    constructor(props){
        super(props)
        this.state = {questions: questions, qIndex:0, corrects:0, incorrects:0, choice: ""}
        this.handleClick = this.handleClick.bind(this)
        this.handleReset = this.handleReset.bind(this)
    }

    handleClick(e){
            this.setState({choice:e.target.value}, ()=>{
                    if (this.state.choice == this.state.questions[this.state.qIndex].answer){
                        this.setState((prevState,props)=>{
                                        return {qIndex: prevState.qIndex+1, corrects: prevState.corrects+1}
                                    })
                    }else{
                        this.setState((prevState,props)=>{
                                    return {qIndex: prevState.qIndex +1, incorrects: prevState.incorrects +1}
                                }, ()=>{
                                    //just for testing purpose
                                        console.log("qIndex= ", this.state.qIndex)
                                        console.log("corrects= ", this.state.corrects)
                                    }
                                )
                    }
                }
            );
    }

    handleReset(){
        return this.setState({qIndex:0})
    }

    render(){
            if (this.state.qIndex >= length){
                return (
                    <div>
                        <Corrects corrects = {this.state.corrects}/>
                        <Incorrects incorrects = {this.state.incorrects}/>
                        <Reset action = {this.handleReset} />
                    </div>
                )
            }  else{
                    return(
                        <div>
                            <Question text ={this.state.questions[this.state.qIndex].q}/>
                            <Choice id ="1" action = {this.handleClick} value = {this.state.questions[this.state.qIndex].choices[0]} />
                            <Choice id ="2" action = {this.handleClick} value = {this.state.questions[this.state.qIndex].choices[1]}/>
                            <Choice id ="3" action = {this.handleClick} value = {this.state.questions[this.state.qIndex].choices[2]}/>
                            <Choice id ="4" action = {this.handleClick} value = {this.state.questions[this.state.qIndex].choices[3]}/>
                            <Corrects corrects = {this.state.corrects}/>
                            <Incorrects incorrects = {this.state.incorrects}/>

                        </div>

                    );
            }
    }
}//End of the class Component

function Question(props){
    return <h1>{props.text}</h1>
}


function Choice(props){
        return <button value = {props.value} onClick ={props.action}> {props.value} </button>
}


function Corrects(props){
        return <p>Correct Answers: {props.corrects}</p>
}


function Incorrects(props){
        return <p>Incorrect Answers: {props.incorrects}</p>
}

function Reset(props){
    return (
        <div>
            <h1> There is no question left, Do you want to try again? </h1>
            <button onClick = {props.action}> Retry </button>
        </div>
    );
}

ReactDOM.render(
            <App  />,
            document.getElementById("root")
)

</script>
