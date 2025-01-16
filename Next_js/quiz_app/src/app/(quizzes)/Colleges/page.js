import Quiz from "@/app/components/quiz";

export default function Colleges() {
    const colleges = [
        {ab: 'CHU', college: 'Churchill'}, 
        {ab: 'G', college: 'Girton'}, 
        {ab: 'M', college: 'Murray Edwards'}, 
        {ab: 'SJC', college: 'St Johns'}, 
        {ab: 'H', college: 'None'}, 
        {ab: 'DOW', college: 'Downing'}, 
        {ab: 'CC', college: 'Corpus Christi'}, 
        {ab: 'HOM', college: 'Homerton'}, 
        {ab: 'CL', college: 'Clare'}, 
        {ab: 'JS', college: 'None'}, 
        {ab: 'DA', college: 'Darwin'}, 
        {ab: 'TH', college: 'Trinity Hall'}, 
        {ab: 'J', college: 'Jesus'}, 
        {ab: 'W', college: 'Wolfson'}, 
        {ab: 'SE', college: 'Selwyn'}, 
        {ab: 'DW', college: 'None'}, 
        {ab: 'M', college: 'Magdalene'}, 
        {ab: 'N', college: 'Newnham'}, 
        {ab: 'PET', college: 'Peterhouse'}, 
        {ab: 'T', college: 'Trinity'}
    ]
    return (
        <Quiz name="Colleges" q={colleges} opt1='ab' opt2='college' />
    );
}