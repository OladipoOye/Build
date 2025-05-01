"use client"
import Link from "next/link";
import { useState } from "react";
import { Stack } from "@chakra-ui/react";
import { HStack } from "@chakra-ui/react";
import { chakra } from "@chakra-ui/react";
import { Slide } from "@chakra-ui/transition";
import { useRef } from "react";

export default function Navigation() {
    // For the menu button toggle
    const [b, setB] = useState(false);
    const [hovered, setHovered] = useState(false); // State to track hover

    const handleClick = () => {
        setB((prev) => !prev);
    };

    const handleMouseOver = () => {
        setHovered(true); // Set hover state to true
    };

    const handleMouseOut = () => {
        setHovered(false); // Set hover state to false
    };

    return (
        <>
            {/* Slide-out menu */}
            <Slide direction="left" w={["80vw", "40vw"]} in={b} style={{ zIndex: 5 }}>
                <Stack h="100vh" w={["100vw", "40vw"]} bgColor="blackAlpha.600" gap={["5vh", "10vh"]}>
                    <Link href="/about">
                        <chakra.p pt="5vh" pl={["40%", "30%"]} textDecor="underline" fontSize={["md", "lg"]}>
                            About
                        </chakra.p>
                    </Link>
                    <Link href="/now">
                        <chakra.p pt="5vh" pl={["40%", "30%"]} textDecor="underline" fontSize={["md", "lg"]}>
                            Now
                        </chakra.p>
                    </Link>
                    <Link href="/contact">
                        <chakra.p pt="5vh" pl={["40%", "30%"]} textDecor="underline" fontSize={["md", "lg"]}>
                            Contact
                        </chakra.p>
                    </Link>
                    <Link href="/">
                        <chakra.p pt="5vh" pl={["40%", "30%"]} textDecor="underline" fontSize={["md", "lg"]}>
                            Freedom
                        </chakra.p>
                    </Link>
                </Stack>
            </Slide>
                    {/* Navigation header */}
            <HStack
                h={["8vh", "8vh"]}
                justifyContent="space-between" 
                alignItems="center" 
                spacing={["4", "8"]} 
                px={["4", "8"]}>                    
                <chakra.h2 fontSize={["md", "xl"]}>
                    Freedom Fellowship
                </chakra.h2>

                    {/* Menu button */}
                <chakra.button
                    w={["12vw", "4vw"]}
                    h={["8vh", "8vh"]}
                    pt={["0.5vh", "0vh"]}
                    cursor="pointer"
                    onClick={handleClick}
                    onMouseOver={handleMouseOver}
                    onMouseOut={handleMouseOut}
                    zIndex="8">
                            
                    <chakra.div
                        transition="0.5s ease-in-out"
                        className="b1"
                        w={["8vw", "3.5vw"]}
                        h="1.5vh"
                        mb="0.4vh"
                        borderRadius="xl"
                        bgColor={b ? "whiteAlpha.600" : "whiteAlpha.950"}
                        transform={[hovered ? "rotate(90deg) scaleY(0.8) scaleX(1.4) translate(1vw, 0.5vh)" : "none", hovered ? "rotate(90deg) scaleY(0.8) translate(1vw, 0.5vh)" : "none"]}>
                    </chakra.div>
                    <chakra.div
                        transition="0.5s ease-in-out"
                        className="b2"
                        w={["8vw", "3.5vw"]}
                        h="1.5vh"
                        mb="0.4vh"
                        borderRadius="xl"
                        bgColor={b ? "whiteAlpha.600" : "whiteAlpha.950"}
                        transform={hovered ? "scale(0.1)" : "none"}>
                    </chakra.div>
                    <chakra.div
                        transition="0.5s ease-in-out"
                        className="b3"
                        w={["8vw", "3.5vw"]}
                        h="1.5vh"
                        borderRadius="xl"
                        bgColor={b ? "whiteAlpha.600" : "whiteAlpha.950"}
                        transform={[hovered ? "scaleY(0.8) translate(-0.6vw, -5vh)" : "none", hovered ? "scaleY(0.8) translate(-0.3vw, -4vh)" : "none"]}>
                    </chakra.div>
                </chakra.button>
            </HStack>
        </>
    );
}