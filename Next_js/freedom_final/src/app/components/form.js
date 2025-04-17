"use client"; // Mark this component as a client component
import { chakra } from "@chakra-ui/react";
import { useState } from "react";

export default function Prayers() {
    const [formData, setFormData] = useState({
        name: "",
        email: "",
        prayer: "",
    });

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    async function handleSubmit(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        try {
            const res = await fetch("https://6781564085151f714b0a5956.mockapi.io/usr", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            });

            if (!res.ok) {
                throw new Error("Failed to submit prayer");
            }

            const newUser = await res.json();
            console.log("Prayer submitted:", newUser);
            alert("Prayer submitted successfully!");
            setFormData({ name: "", email: "", prayer: "" }); // Reset the form
        } catch (error) {
            console.error(error);
            alert("Failed to submit prayer. Please try again.");
        }
    }

    return (
        <>
            <chakra.h4 textDecor="underline">Leave a prayer:</chakra.h4><br/>
            <chakra.form onSubmit={handleSubmit} zIndex="20" display="flex" flexDirection="column" minW="30vw" maxW="50vw">
                <chakra.label>Name (optional):</chakra.label>
                <chakra.input
                    name="name"
                    bgColor="white"
                    color="black"
                    value={formData.name}
                    onChange={handleChange}
                />

                <chakra.label>Email (optional):</chakra.label>
                <chakra.input
                    name="email"
                    bgColor="white"
                    color="black"
                    value={formData.email}
                    onChange={handleChange}
                />

                <chakra.label>Prayer:</chakra.label>
                <chakra.textarea
                    name="prayer"
                    required
                    bgColor="white"
                    color="black"
                    value={formData.prayer}
                    onChange={handleChange}
                />

                <chakra.input type="submit" value="Send" cursor="pointer" />
            </chakra.form>
        </>
    );
}