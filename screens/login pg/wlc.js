import * as React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Image } from 'react-native';



const Wlc = ({ navigation }) => {

    return (
        <View style={styles.bgc} >
            <TouchableOpacity onPress={() => navigation.navigate('Vidd')}>
                <Image
                    source={require('./IMG_0172.PNG')}
                    style={styles.imagee}
                />
            </TouchableOpacity>

        </View>
    );
};


const styles = StyleSheet.create({
    bgc: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor:"#FFEEDB",
    },

    box:{
        width: 1000,
        height: 300,
        paddingTop: 20,
        borderRadius:20,
        backgroundColor:'#FFD0C6',
        alignItems: 'center',
        display:'flex',

    },

    imagee: {
        width: 1180,
        height: 820,
    },



});

  


export default Wlc;