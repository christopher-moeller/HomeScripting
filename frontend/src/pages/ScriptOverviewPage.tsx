import React from "react";
import { Play, Edit, Plus } from "lucide-react";

const scripts = [
  { id: 1, name: "Morning Routine" },
  { id: 2, name: "Turn Off Lights" },
  { id: 3, name: "Party Mode" },
];

const ScriptOverviewPage: React.FC = () => {
    return (
        <div className="flex flex-col items-center justify-start min-h-screen p-8 text-center gap-8 bg-gray-50">
            <div className="w-full max-w-2xl relative">
                <h1 className="text-4xl font-bold mb-2">HomeScripting</h1>
                <p className="text-lg text-gray-600 mb-8">
                Manage and run your smart home scripts from the web.
                </p>

                {/* Add new script */}
                <button className="absolute top-0 right-0 p-2 rounded-xl shadow hover:shadow-md bg-blue-600 text-white hover:bg-blue-700 transition">
                <Plus size={24} />
                </button>

                {/* Script Cards */}
                <div className="flex flex-col gap-4">
                {scripts.map((script) => (
                    <div
                    key={script.id}
                    className="flex justify-between items-center bg-white py-4 px-5 rounded-2xl shadow-sm hover:shadow-md transition cursor-pointer border"
                    >
                    <span className="text-lg font-medium">{script.name}</span>

                    <div className="flex items-center gap-3">
                        {/* Run Button */}
                        <button className="p-2 rounded-lg hover:bg-gray-100 transition">
                        <Play size={20} />
                        </button>

                        {/* Edit Button */}
                        <button className="p-2 rounded-lg hover:bg-gray-100 transition">
                        <Edit size={20} />
                        </button>
                    </div>
                    </div>
                ))}
                </div>
            </div>
        </div>
  );
};

export default ScriptOverviewPage;