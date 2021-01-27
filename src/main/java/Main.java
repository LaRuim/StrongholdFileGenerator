import kaptainwutax.seedutils.mc.MCVersion;
import kaptainwutax.featureutils.structure.generator.StrongholdGenerator;
import kaptainwutax.seedutils.mc.ChunkRand;
import kaptainwutax.seedutils.lcg.rand.JRand;
import java.util.*;
import org.apache.commons.cli.*;

public class Main {
	public static void main(String[] args) {
		Options options = new Options();
		Option random = new Option("r", "random", false, "Use a random World Seed.");
		options.addOption(random);
		Option multiple = new Option("m", "multiple", true, "[NUMBER OF LAYOUTS]");
		options.addOption(multiple);
		Option worldSeed = new Option("s", "world-seed", true, "[WORLD SEED]");
		options.addOption(worldSeed);
		Option chunkX = new Option("x", "chunk-x", true, "[X CO-ORDINATE OF CHUNK]");
		options.addOption(chunkX);
		Option chunkZ = new Option("z", "chunk-z", true, "[Z CO-ORDINATE OF CHUNK]");
		options.addOption(chunkZ);
		Option help = new Option("h", "help", false, "Print this help message and exit (also --help).");
		options.addOption(random);

		CommandLineParser parser = new DefaultParser();
        HelpFormatter formatter = new HelpFormatter();
        CommandLine cmd;

        try {
			cmd = parser.parse(options, args);
			int iters = 1;

			Random rand = new Random();
			long WorldSeed = rand.nextLong();
			int ChunkX = 0;
			int ChunkZ = 0;
	
			if (cmd.hasOption("s") && cmd.hasOption("x") && cmd.hasOption("z")) {
				WorldSeed = Long.parseLong(cmd.getOptionValue("s"));
				ChunkX = Integer.parseInt(cmd.getOptionValue("x"));
				ChunkZ = Integer.parseInt(cmd.getOptionValue("z"));
			}
			else if (cmd.hasOption("r")) {
				if (cmd.hasOption("m")) {
					iters = Integer.parseInt(cmd.getOptionValue("m"));
				}
				WorldSeed = rand.nextLong();
				ChunkX = 0;
				ChunkZ = 0;
			}
	
			else if (cmd.hasOption("h")) {
				formatter.printHelp("Usage: java -jar [filename].jar [options]", options);
				System.out.println("-s requires both -x and -z.");
				System.out.println("-r is incompatible with -s.");
				System.out.println("-m is only available if -r is specified.");
			}
			
			else {
				System.out.println("That combination of command line arguments is invalid.");
				formatter.printHelp("Usage: java -jar [filename].jar [options]", options);
				System.out.println("-s requires both -x and -z.");
				System.out.println("-r is incompatible with -s.");
				System.out.println("-m is only available if -r is specified.");
				System.exit(1);
			}
	
			StrongholdGenerator g = new StrongholdGenerator(MCVersion.v1_16_1);
			ChunkRand r = new ChunkRand();
			
			for (int i = 0; i < iters; i++) {
				g.generate(WorldSeed, ChunkX, ChunkZ, r);
			}
        } catch (ParseException e) {
            System.out.println(e.getMessage());
            formatter.printHelp("Usage: java -jar [filename].jar [options]", options);
			System.out.println("-s requires both -x and -z.");
			System.out.println("-r is incompatible with -s.");
			System.out.println("-m is only available if -r is specified.");
            System.exit(1);
        }

	}
}