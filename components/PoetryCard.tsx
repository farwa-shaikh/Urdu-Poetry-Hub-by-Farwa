import React, { useState } from 'react';
import { Poetry } from '../types';

interface PoetryCardProps {
  poetry: Poetry;
}

export const PoetryCard: React.FC<PoetryCardProps> = ({ poetry }) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    const textToCopy = poetry.lines.join('\n');
    try {
      await navigator.clipboard.writeText(textToCopy);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000); // Reset after 2 seconds
    } catch (err) {
      console.error('Failed to copy text: ', err);
      // Optionally provide user feedback for copy failure
    }
  };

  return (
    <div className="bg-gray-900 rounded-xl shadow-lg p-6 sm:p-8 flex flex-col items-center text-center border border-gray-700 hover:border-gray-500 transition-all duration-300">
      <div className="text-2xl sm:text-3xl font-medium leading-relaxed sm:leading-loose mb-4">
        {poetry.lines.map((line, index) => (
          <p key={index} className="my-1">
            {line}
          </p>
        ))}
      </div>
      {poetry.poet && (
        <p className="text-lg sm:text-xl text-gray-400 mt-2">
          — {poetry.poet}
        </p>
      )}
      <button
        onClick={handleCopy}
        className={`mt-6 px-5 py-2 rounded-lg text-sm sm:text-base font-semibold transition-all duration-300
          ${copied
            ? 'bg-green-600 text-white hover:bg-green-700'
            : 'bg-blue-600 text-white hover:bg-blue-700'
          }`}
      >
        {copied ? 'کاپی ہو گیا! (Copied!)' : 'کاپی کریں (Copy)'}
      </button>
    </div>
  );
};
