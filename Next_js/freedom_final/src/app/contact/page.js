"use client"
import { Box } from "@chakra-ui/react";
import { AspectRatio } from "@chakra-ui/react";
import Prayers from "../components/form";
import { chakra } from "@chakra-ui/react";

export default function Contact() {
    return (
        <>
            <Box>
                
                <chakra.div id="topleft" > 
                    <Prayers />
                </chakra.div>
                
                <AspectRatio>
                    <chakra.iframe src="https://www.youtube.com/@wearefreedomk/" allowFullScreen></chakra.iframe>
                </AspectRatio>
                
                <chakra.div id="bottomleft" >
                    <chakra.p>
                    Service times: Every other wednesday, 7pm<br/>
                    Location: Snoddhurst Bottom, Chatham ME5 OLU<br/>
                    Contact no:
                    </chakra.p>
                </chakra.div>
                
                <AspectRatio>
                    <chakra.iframe src="https://www.instagram.com/wearefreedomkent/embed/" allowFullScreen></chakra.iframe>
                </AspectRatio>
                
            </Box>
        </>
    );
}