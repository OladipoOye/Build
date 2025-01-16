import Link from "next/link";
import { usePathname } from "next/navigation";
import styles from "../ui/navigation.module.css"
import { useState } from "react";



export default function Navigation() {
    const pathname = usePathname(); 
    
    //for the menu button toggle
    const [b, setB] = useState(false);
    
    const handleClick = () => {
        setB((prev) => prev? false: true);
    }
    
    return (
        
        // use Hstack for the links, and a header for the freedom+button
        <>
        
            <div id="sideNav" className={styles.sidenav}>
                <Link className={styles.sidenav_a} href="/about">About</Link>
                <Link className={styles.sidenav_a} href="/now">Now</Link>
                <Link className={styles.sidenav_a} href="/contact">Contact</Link>
                <Link className={styles.sidenav_a} href="/">Freedom</Link>
            </div>
            
            <div className={styles.container}>
                <h2>Freedom Fellowship</h2>

                <button className={styles.i} onClick={handleClick}>
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
