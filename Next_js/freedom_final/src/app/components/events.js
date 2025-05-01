"use client"
import { Box, HStack } from "@chakra-ui/react";
import { chakra } from "@chakra-ui/react";
import { useEffect } from "react";

function hov() {
    //hover function for the event boxes
    const box = document.querySelectorAll(".box");
    box.forEach((b) => {
        b.addEventListener("mouseover", () => {
            b.style.backgroundColor = "white";
            b.style.zIndex = "10";
            b.style.transition = "0.5s";
            b.style.transform = "scale(1.4)";
            b.style.color = "black";
        });
        b.addEventListener("mouseout", () => {
            b.style.backgroundColor = "black";
            b.style.zIndex = "1";
            b.style.transition = "0.5s";
            b.style.transform = "scale(1)";
            b.style.color = "white";
        });
    });
}

export default function Events() {
    useEffect(() => {
        hov(); // Call the hover function after the component mounts
    }, []);
    //event boxes, lined horizontally with images and the descriptions
    return (
        <Box bg="white" w="100%" h="auto" p={["4", "8"]}>
            <chakra.h2
                textAlign="center"
                color="black"
                textDecoration="underline"
                fontSize={["lg", "2xl"]} // Smaller font size for phones
            >
                Events
            </chakra.h2>
            <Box
                display={["block", "flex"]} // Stack vertically on phones, horizontally on larger screens
                flexWrap="wrap"
                justifyContent="center"
                alignItems="center"
                gap={["4", "2vw"]}
                mt="4vh"
            >
                <Box
                    className="box"
                    color="white"
                    w={["90%", "30%"]} // Full width on phones, 30% on larger screens
                    borderRadius="2em"
                    bg="black"
                    h="50vh"
                    mb={["4", "0"]} // Add margin-bottom for spacing on phones
                >
                    <chakra.h3
                        textDecoration="underline"
                        textAlign="center"
                        fontWeight="bold"
                        fontSize={["md", "lg"]}
                    >
                        Event x
                    </chakra.h3>
                    <chakra.img
                        src="#"
                        h="20%"
                        w="80%"
                        alt="event x"
                        mx="auto"
                    />
                    <chakra.p p="8%" fontSize={["sm", "md"]}>
                        Event x is the x event of the year
                        <chakra.br /> covering y and z
                    </chakra.p>
                </Box>
                <Box
                    className="box"
                    color="white"
                    w={["90%", "30%"]}
                    borderRadius="2em"
                    bg="black"
                    h="50vh"
                    mb={["4", "0"]}
                >
                    <chakra.h3
                        textDecoration="underline"
                        textAlign="center"
                        fontWeight="bold"
                        fontSize={["md", "lg"]}
                    >
                        Event y
                    </chakra.h3>
                    <chakra.img
                        src="#"
                        h="20%"
                        w="80%"
                        alt="event y"
                        mx="auto"
                    />
                    <chakra.p p="8%" fontSize={["sm", "md"]}>
                        Event y is the y event of the year
                        <chakra.br /> covering something and something else
                    </chakra.p>
                    </Box>
                <Box
                    className="box"
                    color="white"
                    w={["90%", "30%"]}
                    borderRadius="2em"
                    bg="black"
                    h="50vh"
                    mb={["4", "0"]}
                >
                    <chakra.h3
                        textDecoration="underline"
                        textAlign="center"
                        fontWeight="bold"
                        fontSize={["md", "lg"]}
                    >
                        Event z
                    </chakra.h3>
                    <chakra.img
                        src="#"
                        h="20%"
                        w="80%"
                        alt="event z"
                        mx="auto"
                    />
                    <chakra.p p="8%" fontSize={["sm", "md"]}>
                        Event z is the z event of the year
                        <chakra.br /> allowing for x and z to happen also
                    </chakra.p>
                </Box>
            </Box>
        </Box>
    );
}