import { Poetry } from '../types';
import { STATIC_POETRIES } from '../constants';

/**
 * Simulates fetching a list of two-line Urdu poetries with pagination.
 * In a real application, this would make an API call to a backend with page and limit parameters.
 * @param page The current page number to fetch.
 * @param limit The number of poetries per page.
 * @returns A promise that resolves to an object containing an array of Poetry objects and a boolean indicating if there are more items.
 */
export const fetchPoetries = async (page: number, limit: number): Promise<{ data: Poetry[]; hasMore: boolean }> => {
  return new Promise((resolve) => {
    setTimeout(() => {
      const startIndex = (page - 1) * limit;
      const endIndex = startIndex + limit;
      const data = STATIC_POETRIES.slice(startIndex, endIndex);

      const hasMore = endIndex < STATIC_POETRIES.length;

      resolve({ data, hasMore });
    }, 700); // Simulate network delay
  });
};
