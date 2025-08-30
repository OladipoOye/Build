"use client";
import { Box, Grid, GridItem, AspectRatio, chakra } from "@chakra-ui/react";
import Prayers from "../components/form";

export default function Contact() {
    return (
        <>
            <Box w="100vw" minH="100vh" bgColor="blackAlpha.950" p={["4", "8"]}>
                {/* Responsive Grid Layout */}
                <Grid
                    templateColumns={["1fr", "repeat(2, 1fr)"]} // Adjust columns for different screen sizes
                    gap={["4", "8"]} // Add spacing between grid items
                >
                    {/* Prayer Form */}
                    <GridItem colSpan={[1, 1]} order={[2, 2]}>
                        <Box maxH="60vh" maxW="100%">
                            <Prayers />
                            
                            <chakra.p mt="4vh" fontSize={["md", "xl"]} color="white">
                                Service times: ###ServiceTimes<br />
                                Location: ###Location<br />
                                Contact no: ###ContactNo
                            </chakra.p>
                        </Box>
                    </GridItem>

                    {/* Center Image */}
                    <GridItem colSpan={[1, 1]} order={[1, 1]}>
                        <chakra.img
                            h={["40vh", "60vh"]}
                            w="100%"
                            objectFit="cover"
                            src="/res/ff_0.png"
                            borderRadius="md"
                        />
                    </GridItem>
                    
                    {/* YouTube Embed */}
                    <GridItem colSpan={[1, 1]} order={[3, 3]}>
                        <Box maxH="60vh" maxW="100%">
                            <AspectRatio ratio={16 / 9}>
                                <chakra.iframe
                                    src="https://www.youtube.com/@wearefreedomk/"
                                    allowFullScreen
                                    borderRadius="md"
                                ></chakra.iframe>
                            </AspectRatio>
                        </Box>
                    </GridItem>

                    {/* Instagram Embed */}
                    <GridItem colSpan={[1, 1]} order={[4, 4]}>
                        <Box>
                            <AspectRatio ratio={4 / 3} maxW="80vw" >
                                <chakra.iframe
                                    borderRadius="1em"
                                    src="https://www.instagram.com/wearefreedomkent/embed/"
                                    allowFullScreen
                                ></chakra.iframe>
                            </AspectRatio>
                        </Box>
                    </GridItem>
                </Grid>
            </Box>
        </>
    );
}