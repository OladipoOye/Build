import Quiz from "@/app/components/quiz";

export default function Colleges() {
    const colleges = [
        {ab: 'CHU', college: 'hello'}, 
        {ab: 'G', college: 'hello'}, 
        {ab: 'M', college: 'hello'}, 
        {ab: 'SJC', college: 'hello'}, 
        {ab: 'H', college: 'hello'}, 
        {ab: 'DOW', college: 'hello'}, 
        {ab: 'accueillir', college: 'hello'}, 
        {ab: 'HOM', college: 'hello'}, 
        {ab: 'mettre', college: 'hello'}, 
        {ab: 'JS', college: 'None'}, 
        {ab: 'W', college: 'hello'}, 
        {ab: 'SE', college: 'hello'}, 
        {ab: 'se sentir', college: 'hello'}, 
        {ab: 'tirer', college: 'hello'}, 
        {ab: 'T', college: 'hello'}
    ]
    return (
        <Quiz name="Colleges" q={colleges} opt1='ab' opt2='college' />
    );
}