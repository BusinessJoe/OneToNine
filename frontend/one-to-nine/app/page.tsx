import Sudoku from './sudoku/Sudoku';

export default function Home() {

	return (
		<main className='flex max-h-screen flex-col items-center justify-between'>
			<Sudoku />
		</main>
	);
}
