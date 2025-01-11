import Link from "next/link";
import { usePathname } from "next/navigation";

export default function Navigation() {
    const pathname = usePathname(); 
        
    return (
        <nav>
            <Link href="/about">About</Link>
            <Link href="/now">Now</Link>
            <Link href="/contact">Contact</Link>
            <Link href="/">Freedom</Link>
        </nav>);}
