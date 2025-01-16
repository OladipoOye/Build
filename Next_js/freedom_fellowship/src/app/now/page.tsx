import styles from "../ui/now.module.css"

export default function Now() {
    //create animation upon entering page of the pop up for the theme of the month, try to divide it and apply a border radius to get the sam effect
    //the animation should be pop-up like, and ease-in
    //the rest of the page can stay the same
    //rework the modals using state to avoid excess css
    return (
        <>
            <head>
                <meta charSet="UTF-8"/>
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <meta name="description" content="Now in Freedom"/>
                <title>Now in Freedom</title>
            </head>
            <body>
                <div id="Modal_box" className={styles.modal}>
                    <span className={styles.close}>&times;</span>
                    <img className={styles.modal_content} id="modal_img"/>
                    <div className={styles.caption} id="caption"></div>
                </div>

                <div className={styles.bg_img}>
                    <img src="../res/ff_2.jpg"/>
                    <div className={styles.bottom_left} ><h1 className={styles.small_modal} >Ch3</h1></div>
                    <div className={styles.top_left} >
                        <img src="../res/Proverbs21_2.png" className={styles.small_modal} id="Prov" />
                    </div>
                    <div className={styles.top_right}><h1 className={styles.small_modal} >Ch1</h1></div>
                    <div className={styles.bottom_right}><h1 className={styles.small_modal} >Ch2</h1></div>
                    <div className={styles.centered}><h2>Theme Of The <br/>Month</h2></div>
                </div>
            </body>
        </>
    );
}