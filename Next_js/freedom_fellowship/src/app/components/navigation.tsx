import Link from "next/link";
import { usePathname } from "next/navigation";
import styles from "../ui/navigation.module.css"



export default function Navigation() {
    const pathname = usePathname(); 
    
    // for the menu button toggle
    function togg() {
        const i = document.querySelector('.i');
        if (i.className == 'i is-active') {openNav()}
        else {closeNav()}
        i.classList.toggle('is-active');};

    // opening the nav bar
    function openNav(){
        document.getElementById('sideNav').style.width = '25%';}
        //document.body.style.backgroundColor = 'rgba(0,0,0,0.4)'}}

    function closeNav(){
        document.getElementById('sideNav').style.width = '0px';}
        //document.body.style.backgroundColor = 'white'}
    
    return (
        <>
            <div id="sideNav" className={styles.sidenav}>
                <Link className={styles.sidenav_a} href="/about">About</Link>
                <Link className={styles.sidenav_a} href="/now">Now</Link>
                <Link className={styles.sidenav_a} href="/contact">Contact</Link>
                <Link className={styles.sidenav_a} href="/">Freedom</Link>
            </div>
            
            <div className={styles.container}>
                <h2>Freedom Fellowship</h2>

                <button className={styles.i} onClick={togg}>
                    <span></span>
                    <span></span>
                    <span></span> 
                </button>
            </div>
            <nav>
            <Link href="/about">About</Link>
            <Link href="/now">Now</Link>
            <Link href="/contact">Contact</Link>
            <Link href="/">Freedom</Link>
        </nav>
    </>);}
