import Quiz from "@/app/components/quiz";

export default function French() {
    const french = [
        {fr: 'sauter', en: 'hello'}, 
        {fr: 'aller', en: 'hello'}, 
        {fr: 'sauveguarder', en: 'hello'}, 
        {fr: 'lever', en: 'hello'}, 
        {fr: 'guerir', en: 'hello'}, 
        {fr: 'subventionner', en: 'hello'}, 
        {fr: 'accueillir', en: 'hello'}, 
        {fr: 'prendre', en: 'hello'}, 
        {fr: 'mettre', en: 'hello'}, 
        {fr: 'courrir', en: 'hello'}, 
        {fr: 'aggrandir', en: 'hello'}, 
        {fr: 'ameliorer', en: 'hello'}, 
        {fr: 'se sentir', en: 'hello'}, 
        {fr: 'tirer', en: 'hello'}, 
        {fr: 'criore', en: 'hello'}, 
    ]
    return (
        <Quiz name="French" q={french} opt1='fr' opt2='en' />
    );
}