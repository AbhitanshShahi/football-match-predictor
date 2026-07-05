export default function Loader() {
  return (
    <div className="flex flex-col items-center justify-center py-12">
      <div className="relative">
        <div className="w-20 h-20 border-4 border-white/20 border-t-yellow-400 rounded-full animate-spin"></div>
        <div className="absolute inset-0 flex items-center justify-center text-5xl animate-bounce">
          ⚽
        </div>
      </div>
      <p className="text-emerald-300 mt-6 font-medium tracking-widest">
        ANALYZING TACTICS...
      </p>
    </div>
  );
}
