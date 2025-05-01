import { Box } from "@chakra-ui/react";

export default function Home() {
  return (
    <>
      <Box
        h={["50vh", "110vh"]} // Height: 50vh for small screens, 110vh for larger screens
        opacity="0.9"
        bgPos={["top", "center"]} // Background position: "top" for small screens, "center" for larger screens
        bgAttachment={["scroll", "fixed"]} // Background attachment: "scroll" for small screens, "fixed" for larger screens
        bgRepeat="no-repeat"
        bgSize="cover"
        bgImage="url(/res/ff_0.png)"
      ></Box>
      <Box
        h={["50vh", "110vh"]}
        opacity="0.9"
        bgPos={["top", "center"]}
        bgAttachment={["scroll", "fixed"]}
        bgRepeat="no-repeat"
        bgSize="cover"
        bgImage="url(/res/Issac.png)"
      ></Box>
      <Box
        h={["50vh", "110vh"]}
        opacity="0.9"
        bgPos={["top", "top"]}
        bgAttachment={["scroll", "fixed"]}
        bgRepeat="no-repeat"
        bgSize="cover"
        bgImage="url(/res/Aunties.png)"
        ></Box>
      <Box
        h={["50vh", "110vh"]}
        opacity="0.9"
        bgPos={["top", "center"]}
        bgAttachment={["scroll", "fixed"]}
        bgRepeat="no-repeat"
        bgSize="cover"
        bgImage="url(/res/ff_1.jpg)"
      ></Box>
      <Box
        h={["50vh", "110vh"]}
        opacity="0.9"
        bgPos={["top", "top"]}
        bgAttachment={["scroll", "fixed"]}
        bgRepeat="no-repeat"
        bgSize="cover"
        bgImage="url(/res/Aunt.png)"
      ></Box>
      <Box
        h={["50vh", "110vh"]}
        opacity="0.9"
        bgPos={["top", "top"]}
        bgAttachment={["scroll", "fixed"]}
        bgRepeat="no-repeat"
        bgSize="cover"
        bgImage="url(/res/Unc.png)"
      ></Box>
    </>
  );
}