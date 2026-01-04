import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { useEffect, useState } from "react";

export default function Home() {
    const navigate = useNavigate(); 
    return (
        <motion.div
            initial={{ opacity:0, y:20 }}
            animate={{ opacity:1, y: 0 }}
            className="text-center space-y-8 max-w-2xl px-6"
        >
            <div className="space-y-4">
                <h1 className="text-5xl font-extrabold tracking-tight lg:text-7xl bg-gradient-to-r from-blue-400 to-emerald-400 bg-clip-text text-transparent">IT Career</h1>
                <p className="text-slate-400 text-xl leading-relaxed">"Your career doesn’t define your worth, but it can reflect your values."</p>
            </div> 

            <Button size="lg" onClick={() => navigate('/quiz')} className="text-lg px-10 py-6 rounded-full shadow-lg shadow-blue-500/20 hover:shadow-blue-500/40 transition-all duration-300">
                Mulai
            </Button>

        </motion.div>
    )
}