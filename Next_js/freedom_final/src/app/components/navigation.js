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

    const handleClick = () => {
        setB((prev) => !prev);
    };

    // Use refs for the menu button divs
    const b1Ref = useRef(null);
    const b2Ref = useRef(null);
    const b3Ref = useRef(null);

    // For the menu button animation
    function handleMouseOver() {
        if (b1Ref.current && b2Ref.current && b3Ref.current) {
            b1Ref.current.style.transform = "rotate(90deg) scaleX(1.3) scaleY(0.8) translate(1vw, 0.5vh)";
            b2Ref.current.style.transform = "scale(0)";
            b3Ref.current.style.transform = "scaleY(0.8) translate(-0.5vw, -4vh)";
        }
    }

    function handleMouseOut() {
        if (b1Ref.current && b2Ref.current && b3Ref.current) {
            b1Ref.current.style.transform = "rotate(0deg) scaleX(1) translate(0vw, 0vh)";
            b2Ref.current.style.transform = "scale(1)";
            b3Ref.current.style.transform = "scaleX(1) scaleY(1) translate(0vw, 0vh)";
        }
    }

    return (
        <>
            <Slide direction="left" w="40vw" in={b} style={{ zIndex: 5 }}>
                <Stack h="100vh" w="40vw" bgColor="blackAlpha.600" gap="10vh">
                    <Link href="/about"><chakra.p pt="5vh" pl="30%" textDecor="underline"> About </chakra.p></Link>
                    <Link href="/now"><chakra.p pt="5vh" pl="30%" textDecor="underline"> Now </chakra.p></Link>
                    <Link href="/contact"><chakra.p pt="5vh" pl="30%" textDecor="underline"> Contact </chakra.p></Link>
                    <Link href="/"><chakra.p pt="5vh" pl="30%" textDecor="underline"> Freedom </chakra.p></Link>
                </Stack>
            </Slide>

            <HStack>
                <chakra.h2 pt="3vh" pl="1vw" h="10vh" fontSize="xl">Freedom Fellowship</chakra.h2>

                <chakra.button
                    ml="80vw"
                    w="8vw"
                    h="6vh"
                    cursor="pointer"
                    onClick={handleClick}
                    onMouseOver={handleMouseOver}
                    onMouseOut={handleMouseOut}
                    zIndex="8"
                >
                    <chakra.div ref={b1Ref} transition="0.5s ease-in-out" className="b1" w="3.5vw" h="1.5vh" mb="0.4vh" borderRadius="xl" bgColor={b ? "whiteAlpha.600" : "whiteAlpha.950"}></chakra.div>
                    <chakra.div ref={b2Ref} transition="0.5s ease-in-out" className="b2" w="3.5vw" h="1.5vh" mb="0.4vh" borderRadius="xl" bgColor={b ? "whiteAlpha.600" : "whiteAlpha.950"}></chakra.div>
                    <chakra.div ref={b3Ref} transition="0.5s ease-in-out" className="b3" w="3.5vw" h="1.5vh" borderRadius="xl" bgColor={b ? "whiteAlpha.600" : "whiteAlpha.950"}></chakra.div>
                </chakra.button>
            </HStack>
        </>
    );
}