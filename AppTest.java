package com.example;

import static org.junit.Assert.*;
import org.junit.Test;

public class AppTest {
    App myApp = new App();

    @Test
    public void testLogic() {
        // Test AND: True + True = True
        assertTrue(myApp.checkAccess(true, true));
        
        // Test OR: False + True = True
        assertTrue(myApp.canEnter(false, true));
        
        // Test NOT: Not True = False
        assertFalse(myApp.isDoorLocked(true));
    }
}
