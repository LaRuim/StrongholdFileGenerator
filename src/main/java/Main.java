import kaptainwutax.seedutils.mc.MCVersion;
import kaptainwutax.featureutils.structure.generator.StrongholdGenerator;
import kaptainwutax.seedutils.mc.ChunkRand;
import kaptainwutax.seedutils.lcg.rand.JRand;
import java.util.*;

public class Main {
	public static void main(String[] args) {
		StrongholdGenerator g = new StrongholdGenerator(MCVersion.v1_16_1);
		ChunkRand r = new ChunkRand();
		Random rand = new Random();
		Scanner input = new Scanner(System.in);
		System.out.println("World seed: ");
		long worldSeed = input.nextLong();
		System.out.println("Chunk X: ");
		int chunkX = input.nextInt();
		System.out.println("Chunk Z: ");
		int chunkZ = input.nextInt();
		g.generate(worldSeed, chunkX, chunkZ, r);
	}
}