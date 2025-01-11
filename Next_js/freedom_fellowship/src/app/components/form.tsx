import { revalidatePath } from "next/cache";
import styles from "../ui/form.module.css"

export default async function Prayers() {
    const response = await fetch("https://6781564085151f714b0a5956.mockapi.io/usr");
    const usrs = await response.json();
    
    async function addUser(formData: FormData) {
        "use server"
        const name = formData.get("name")
        const res = await fetch("https://6781564085151f714b0a5956.mockapi.io/usr",
            {
                method: "POST",
                headers: {
                    "Content-Type":"application/json"
                }, 
                body: JSON.stringify({ name }), }
            );
        const newUser = await res.json();
        revalidatePath("/mock-users");
        //console.log(newUser)
    };
    
    return(
        <>
            <form className={styles.formStyle} action={addUser}>
                <label className={styles.labelStyle} >Name (optional):</label>
                <input className={styles.sInputStyle} name="user_name" />
          
                <label className={styles.labelStyle} >Email (optional):</label>
                <input className={styles.sInputStyle} name="user_email" />
          
                <label className={styles.labelStyle}>Prayer</label>
                <textarea className={styles.lInputStyle} name="message" required/>
          
                <input className={styles.buttonStyle} type="submit" value="Send" />
            </form>
        </>
    );
}