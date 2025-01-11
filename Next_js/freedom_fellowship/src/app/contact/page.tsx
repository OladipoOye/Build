import styles from "../ui/contact.module.css"
import Prayers from "../components/form";

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
            <div className={styles.hero_img}>
                <div className={styles.top_left}>
                    Leave a prayer: <br/><br/>
                    <Prayers />
                </div>
            
                <div className={styles.bottom_left}>
                    Service times: Every other wednesday, 7pm<br/>
                    Location: Snoddhurst Bottom, Chatham ME5 OLU<br/>
                    Contact no: <br/><br/>
                </div>

                <div className={styles.top_right}>
                    <br/>
                    <a className={styles.dont} target="_blank" href="https://www.youtube.com/@wearefreedomk/">
                        <img src="../res/yt_logo_mono_dark.png"/>
                    </a>
                </div>
            
                <div className={styles.bottom_right}>
                    <iframe src="https://www.instagram.com/wearefreedomkent/embed/" allowFullScreen></iframe>
                </div>
            
                <div className={styles.centered}>
                    <img src="../res/ff_0.png" id="free"/>
                </div>
            </div>
            
        </body>
    </>  
    );
}