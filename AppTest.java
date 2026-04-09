package com.app;
import static org.junit.Assert.*;
import org.junit.Test;

public class AppTest {
    App app = new App();
    @Test
    public void testLogic() {
        assertTrue("AND logic failed", app.evaluateAND(true, true));
        assertTrue("OR logic failed", app.evaluateOR(true, false));
        assertFalse("NOT logic failed", app.evaluateNOT(true));
    }
}
