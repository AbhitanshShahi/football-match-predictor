import { teams } from "../utils/data";
import { Users } from "lucide-react";

type Props = {
  home: string;
  away: string;
  setHome: (v: string) => void;
  setAway: (v: string) => void;
};

export default function TeamSelector({ home, away, setHome, setAway }: Props) {
  return (
    <div className="space-y-6">
      <div className="flex items-center gap-3 text-emerald-300 mb-4">
        <Users className="w-6 h-6" />
        <h2 className="uppercase tracking-[3px] text-sm font-semibold">
          Select Teams
        </h2>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Home Team */}
        <div>
          <div className="flex items-center gap-2 mb-2 text-sm text-emerald-400">
            <div className="px-3 py-1 bg-emerald-600/30 rounded-full">HOME</div>
            <span className="font-mono text-xs">TEAM A</span>
          </div>
          <select
            className="w-full bg-white/10 border border-white/20 text-white rounded-2xl px-6 py-5 text-xl font-semibold focus:outline-none focus:border-yellow-400 transition-all appearance-none cursor-pointer hover:bg-white/15"
            value={home}
            onChange={(e) => setHome(e.target.value)}
          >
            <option value="" className="bg-emerald-950 text-white">
              Select Home Team
            </option>
            {teams.map((t) => (
              <option key={t} value={t} className="bg-emerald-950 text-white">
                {t}
              </option>
            ))}
          </select>
        </div>

        {/* Away Team */}
        <div>
          <div className="flex items-center gap-2 mb-2 text-sm text-emerald-400">
            <div className="px-3 py-1 bg-rose-600/30 rounded-full">AWAY</div>
            <span className="font-mono text-xs">TEAM B</span>
          </div>
          <select
            className="w-full bg-white/10 border border-white/20 text-white rounded-2xl px-6 py-5 text-xl font-semibold focus:outline-none focus:border-yellow-400 transition-all appearance-none cursor-pointer hover:bg-white/15"
            value={away}
            onChange={(e) => setAway(e.target.value)}
          >
            <option value="" className="bg-emerald-950 text-white">
              Select Away Team
            </option>
            {teams.map((t) => (
              <option key={t} value={t} className="bg-emerald-950 text-white">
                {t}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* VS Badge */}
      <div className="flex justify-center -my-4">
        <div className="bg-emerald-950 border-4 border-yellow-400 text-yellow-400 text-4xl font-black px-8 py-2 rounded-2xl shadow-inner">
          VS
        </div>
      </div>
    </div>
  );
}
