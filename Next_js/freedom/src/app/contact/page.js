import Prayers from "../components/form.js";

export default function Contact() {
    
    return(
    <>
        <head>
            <meta charSet="UTF-8" />
            <meta name="description" content="Contacting Freedom" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Contact Freedom</title>
        </head>
        <body>    
            <div >
                <div >
                    Leave a prayer: <br/><br/>
                    <Prayers />
                </div>
            
                <div >
                    Service times: Every other wednesday, 7pm<br/>
                    Location: Snoddhurst Bottom, Chatham ME5 OLU<br/>
                    Contact no: <br/><br/>
                </div>

                <div >
                    <br/>
                    <a target="_blank" href="https://www.youtube.com/@wearefreedomk/">
                        <img src="#"/>
                    </a>
                </div>
            
                <div >
                    <iframe src="https://www.instagram.com/wearefreedomkent/embed/" allowFullScreen></iframe>
                </div>
            
                <div >
                    <img src="#" id="free"/>
                </div>
            </div>
            
        </body>
    </>  
    );
}