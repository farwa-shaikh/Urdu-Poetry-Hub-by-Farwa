import React, { useState, useEffect, useCallback, useRef } from 'react';
import { Poetry } from './types';
import { fetchPoetries } from './services/poetryService';
import { PoetryCard } from './components/PoetryCard';

const POETRIES_PER_PAGE = 5; // Define how many poetries to load per page

const App: React.FC = () => {
  const [poetries, setPoetries] = useState<Poetry[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [hasMore, setHasMore] = useState<boolean>(true); // Indicates if there are more poetries to load
  const loaderRef = useRef<HTMLDivElement>(null); // Ref for the infinite scroll loader

  const loadPoetries = useCallback(async (page: number) => {
    // Only show full-screen loader for the very first load
    // For subsequent loads (infinite scroll), show the bottom loader
    if (page === 1) {
      setLoading(true);
    }
    setError(null);
    try {
      const { data, hasMore: newHasMore } = await fetchPoetries(page, POETRIES_PER_PAGE);

      setPoetries((prevPoetries) => {
        // Filter out duplicates if any, based on id (important for retries)
        const newPoetries = data.filter(
          (newPoetry) => !prevPoetries.some((existingPoetry) => existingPoetry.id === newPoetry.id)
        );
        return [...prevPoetries, ...newPoetries];
      });
      setHasMore(newHasMore);
    } catch (err: any) {
      console.error("Failed to fetch poetries:", err);
      setError(`Failed to load poetries: ${err.message || 'Unknown error'}`);
      setHasMore(false); // Stop trying to load more if there's an error
    } finally {
      setLoading(false); // Always set loading to false after fetch attempt
    }
  }, []);

  // Initial load
  useEffect(() => {
    loadPoetries(1);
  }, [loadPoetries]);

  // Infinite scroll observer
  useEffect(() => {
    const options = {
      root: null, // viewport
      rootMargin: '200px', // fetch when 200px from bottom
      threshold: 1.0,
    };

    const observer = new IntersectionObserver((entries) => {
      const target = entries[0];
      if (target.isIntersecting && hasMore && !loading) {
        setCurrentPage((prevPage) => prevPage + 1);
      }
    }, options);

    if (loaderRef.current) {
      observer.observe(loaderRef.current);
    }

    return () => {
      if (loaderRef.current) {
        observer.unobserve(loaderRef.current);
      }
    };
  }, [hasMore, loading]); // Depend on hasMore and loading to prevent unnecessary triggers

  // Effect to load poetries when currentPage changes (triggered by observer)
  useEffect(() => {
    if (currentPage > 1) { // Don't trigger for the initial page load (handled by first useEffect)
      loadPoetries(currentPage);
    }
  }, [currentPage, loadPoetries]);


  return (
    <div className="min-h-screen bg-black text-white flex flex-col items-center p-4 sm:p-6 md:p-8 lg:p-10">
      <header className="w-full text-center py-6 sm:py-8 md:py-10">
        <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold mb-2 leading-tight">
          اردو شاعری
        </h1>
        <p className="text-xl sm:text-2xl text-gray-300">
          انتخابِ بہترین دو سطر شاعری
        </p>
      </header>

      <main className="w-full max-w-2xl flex-grow flex flex-col items-center">
        {/* Initial loading screen or error for the first page */}
        {(loading && currentPage === 1) && (
          <div className="flex items-center justify-center p-8 text-2xl text-gray-400">
            <svg className="animate-spin -ml-1 mr-3 h-8 w-8 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            لوڈنگ شاعری...
          </div>
        )}

        {error && (
          <div className="bg-red-800 text-red-100 p-4 rounded-lg text-center text-lg mt-8">
            <p className="font-bold mb-2">خرابی! (Error!)</p>
            <p>{error}</p>
            <button
              onClick={() => loadPoetries(currentPage)} // Retry the current page
              className="mt-4 px-6 py-2 bg-red-600 hover:bg-red-700 text-white font-semibold rounded-lg transition duration-200"
            >
              دوبارہ کوشش کریں (Try Again)
            </button>
          </div>
        )}

        {/* Display poetries */}
        {poetries.length > 0 && (
          <div className="w-full grid gap-6 md:gap-8 lg:gap-10 py-6 sm:py-8">
            {poetries.map((poetry) => (
              <PoetryCard key={poetry.id} poetry={poetry} />
            ))}
          </div>
        )}

        {/* Infinite scroll loader / End of list message */}
        <div ref={loaderRef} className="w-full py-8 text-center">
          {(loading && currentPage > 1 && hasMore) && ( // Show loader for subsequent pages
            <div className="flex items-center justify-center text-2xl text-gray-400">
              <svg className="animate-spin -ml-1 mr-3 h-8 w-8 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              لوڈنگ مزید شاعری...
            </div>
          )}
          {(!hasMore && poetries.length > 0 && !loading) && ( // End of list message
            <p className="text-xl text-gray-500">تمام شاعری ختم ہو گئی (End of all poetry).</p>
          )}
          {(!loading && !error && poetries.length === 0 && !hasMore) && ( // No poetry at all
            <p className="p-8 text-xl text-gray-400">کوئی شاعری نہیں ملی۔ (No poetry found.)</p>
          )}
        </div>
      </main>

      <footer className="w-full text-center py-4 sm:py-6 text-gray-500 text-sm mt-8">
        <p>© {new Date().getFullYear()} اردو شاعری Hub. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default App;