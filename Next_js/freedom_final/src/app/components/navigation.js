"use client"
import Link from "next/link";
import { useState } from "react";
import { HStack } from "@chakra-ui/react";
import { chakra } from "@chakra-ui/react";
import { Slide } from "@chakra-ui/transition";

export default function Navigation() {
    
    //for the menu button toggle
    const [b, setB] = useState(false);
    
    const handleClick = () => {
        setB((prev) => prev? false : true)
    };
    
    return (
        <>
        <Slide direction="left" in={b} style={{zIndex: 5}}>
            <HStack>
                <Link href="/about">About</Link>
                <Link href="/now">Now</Link>
                <Link href="/cotact">Contact</Link>
                <Link href="/">Freedom</Link>
            </HStack>
        </Slide>
        
        <chakra.div>
            <chakra.h2>Freedom Fellowship</chakra.h2>
            
            <chakra.button cursor="pointer" onClick={handleClick}>
                <chakra.span bg="white" ></chakra.span>
                <chakra.span bg="white" ></chakra.span>
                <chakra.span bg="white" ></chakra.span>
            </chakra.button>
        </chakra.div>
        
        </>
    )
}