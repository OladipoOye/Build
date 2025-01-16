"use client"
import Link from "next/link";
//import styles from "../ui/navigation.module.css"
import { useState } from "react";
import { HStack } from "@chakra-ui/react";
import { chakra } from "@chakra-ui/react";
import { Slide } from '@chakra-ui/transition';



export default function Navigation() {
    
    //for the menu button toggle
    const [b, setB] = useState(false);
    
    const handleClick = () => {
        setB((prev) => prev? false: true);
    }
    
    return (
        /* restyle and come back to
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
        */
        // use Hstack for the links, and a header for the freedom+button
        <>
            <Slide direction="left" in={b} style={{zIndex: 5}}>
                <HStack>
                    <Link href="/about">About</Link>
                    <Link href="/now">Now</Link>
                    <Link href="/contact">Contact</Link>
                    <Link href="/">Freedom</Link>
                </HStack>
            </Slide>
            
            <chakra.div>
                <chakra.h2> Freedom Fellowship</chakra.h2>
                
                <chakra.button bg="white" cursor='pointer' onClick={handleClick}>
                    <span></span>
                    <span></span>
                    <span></span> 
                </chakra.button>
            </chakra.div>
        
            
    </>);}
