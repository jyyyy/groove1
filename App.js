import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import Wlc from './screens/login pg/wlc';
import Vidd from './screens/login pg/vidd';
import Login0 from './screens/login pg/login0';
import Login1 from './screens/login pg/login1';
import NoAcc from './screens/home pg/noacc';
import Accpg from './screens/home pg/accpg';
import Fave from './screens/home pg/fave';
import CreateAcc from './screens/create/createacc';

const Stack = createStackNavigator();

const App = () => {

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home" screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Wlc" component={Wlc} />
        <Stack.Screen name="Vidd" component={Vidd} />
        <Stack.Screen name="Login0" component={Login0} />
        <Stack.Screen name="Login1" component={Login1} />
        <Stack.Screen name="NoAcc" component={NoAcc} />
        <Stack.Screen name="Accpg" component={Accpg} />
        <Stack.Screen name="Fave" component={Fave} />
        <Stack.Screen name="CreateAcc" component={CreateAcc} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};



export default App;
